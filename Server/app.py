#imports
from flask import Flask, make_response,request,jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required,  get_jwt_identity, current_user
from models import db,User, Listing, Location, Property, RentalTerms, Review, UserFavoriteProperty 



# initiasing app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '332nsdbd993h3bd84920'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '3dw72g32@#!'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)  # Access token expiration time (1 hour in this example)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

migrate =Migrate(app,db) 
db.init_app(app)
api = Api(app)

jwt = JWTManager(app)




class UserResource(Resource):
    def get(self):
        user_list = [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'hashed_password': user.hashed_password,
            'role': user.role,
            'registration_date': user.registration_date.strftime("%Y-%m-%d %H:%M:%S")  
        } for user in User.query.all()]

        # Include the access token in the response data
        access_token = create_access_token(identity="some_identity")  # You can pass the user's identity here
        response_data = {
            'users': user_list,
            'access_token': access_token
        }

        return response_data, 200

    
    def post(self):
        data = request.get_json()

        username = data.get('username')
        email = data.get('email')
        password = data.get('hashed_password')
        role = data.get('role')

        # Check if the email or username already exist in the backend
        existing_email_user = User.query.filter_by(email=email).first()
        existing_username_user = User.query.filter_by(username=username).first()

        if existing_email_user:
            return {'message': 'Email already exists'}, 409

        if existing_username_user:
            return {'message': 'Username already exists'}, 409

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, email=email, hashed_password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user.id)

        response_data = {
            'message': 'User created successfully',
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                'hashed_password': new_user.hashed_password,
                'role': new_user.role,
                'registration_date': new_user.registration_date.strftime("%Y-%m-%d %H:%M:%S")
            },
            'access_token': access_token  # generated access token
        }
        return response_data, 201




 
 
 
 
 
class UserResourceId(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            user_data = user.to_dict()

            # addeds access token in the response data
            access_token = create_access_token(identity=user.id)  
            response_data = {
                'user': user_data,
                'access_token': access_token
            }

            return response_data, 200
        else:
            return {'message': 'User not found'}, 404

    def patch(self, user_id):
        user = User.query.get(user_id)
        if user:
            data = request.get_json()

            # Hash the new password before updating it in the database
            new_password = data.get('hashed_password')
            if new_password:
                hashed_password = generate_password_hash(new_password)
                user.hashed_password = hashed_password

            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.role = data.get('role', user.role)
            db.session.commit()
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

class CheckUsernameAndEmail(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        response_data = {
            'usernameExists': False,
            'emailExists': False,
        }

        if existing_user:
            if existing_user.username == username:
                response_data['usernameExists'] = True
            if existing_user.email == email:
                response_data['emailExists'] = True

        return response_data


# Add the resource to the API with the desired endpoint
api.add_resource(CheckUsernameAndEmail, '/check_username_and_email')

class UserLoginResource(Resource):
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')  # Use 'password' instead of 'hashed_password'

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        # Check if the user with the provided email exists
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'message': 'User not found'}, 404

        # Verify the provided password against the hashed password in the database
        if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return {'message': 'Invalid credentials'}, 401

        # Generate access token if the login is successful
        access_token = create_access_token(identity=user.id)

        response_data = {
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'registration_date': user.registration_date.isoformat()
            },
            'access_token': access_token
        }

        return response_data, 200

api.add_resource(UserLoginResource, '/login')



class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'You are authorized to access this protected resource.'}, 200
    
api.add_resource(ProtectedResource, '/protected')

#property access
class PropertyResource(Resource):
    def get(self):
        properties = Property.query.all()
        property_list = [
            # {
            #     'id': property.id,
            #     'property_type': property.property_type,
            #     'property_category': property.property_category,
            #     'bedrooms': property.bedrooms,
            #     'bathrooms': property.bathrooms,
            #     'square_footage': property.square_footage,
            #     'media': property.media,
            #     'furnished': property.furnished,
            #     'description': property.description,
            #     'location_details': property.location_details,
            #     'landlord_name': property.landlord_name,
            #     'contact_phone': property.contact_phone,
            #     'contact_email': property.contact_email,
            #     'preferred_contact_method': property.preferred_contact_method,
            #     'additional_details': property.additional_details,
            # }
            property.to_dict() for property in properties
        ]
        response= make_response( property_list,200)
        
        return response
    
    def post(self):
        # Get the JSON data from the request
        data = request.get_json()

        # Extract the required fields from the JSON data
        property_type = data.get('property_type')
        property_category = data.get('property_category')
        bedrooms = data.get('bedrooms')
        bathrooms = data.get('bathrooms')
        square_footage = data.get('square_footage')
        media = data.get('media')
        furnished = data.get('furnished', 'Y')
        description = data.get('description')
        location_details = data.get('location_details')
        landlord_name = data.get('landlord_name')
        contact_phone = data.get('contact_phone')
        contact_email = data.get('contact_email')
        preferred_contact_method = data.get('preferred_contact_method')
        additional_details = data.get('additional_details')

        # Create a new Property object and add it to the database
        new_property = Property(
            property_type=property_type,
            property_category=property_category,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_footage=square_footage,
            media=media,
            furnished=furnished,
            description=description,
            location_details=location_details,
            landlord_name=landlord_name,
            contact_phone=contact_phone,
            contact_email=contact_email,
            preferred_contact_method=preferred_contact_method,
            additional_details=additional_details,
        )
        db.session.add(new_property)
        db.session.commit()

        # Prepare the success message
        success_message = f"Property with ID {new_property.id} has been successfully created."

        return {
            'message': success_message,
            'id': new_property.id,
            'property_type': new_property.property_type,
            'property_category': new_property.property_category,
            'bedrooms': new_property.bedrooms,
            'bathrooms': new_property.bathrooms,
            'square_footage': new_property.square_footage,
            'media': new_property.media,
            'furnished': new_property.furnished,
            'description': new_property.description,
            'location_details': new_property.location_details,
            'landlord_name': new_property.landlord_name,
            'contact_phone': new_property.contact_phone,
            'contact_email': new_property.contact_email,
            'preferred_contact_method': new_property.preferred_contact_method,
            'additional_details': new_property.additional_details,
        }, 201  # 201 Created status code




class PropertyResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all properties
            properties = Property.query.all()
            property_list = [
                {
                    'id': property.id,
                    'property_type': property.property_type,
                    'bedrooms': property.bedrooms,
                    'bathrooms': property.bathrooms,
                    'square_footage': property.square_footage,
                    'media': property.media,
                    'furnished': property.furnished,
                    'description': property.description,
                    'location_details': property.location_details,
                    'landlord_name': property.landlord_name,
                    'contact_phone': property.contact_phone,
                    'contact_email': property.contact_email,
                    'preferred_contact_method': property.preferred_contact_method,
                    'additional_details': property.additional_details,
                }
                for property in properties
            ]
            return property_list
        else:
            # If id is provided, return a specific property by ID
            property = Property.query.get(id)
            if property:
                return {
                    'id': property.id,
                    'property_type': property.property_type,
                    'bedrooms': property.bedrooms,
                    'bathrooms': property.bathrooms,
                    'square_footage': property.square_footage,
                    'media': property.media,
                    'furnished': property.furnished,
                    'description': property.description,
                    'location_details': property.location_details,
                    'landlord_name': property.landlord_name,
                    'contact_phone': property.contact_phone,
                    'contact_email': property.contact_email,
                    'preferred_contact_method': property.preferred_contact_method,
                    'additional_details': property.additional_details,
                }
            else:
                return {'message': 'Property not found'}, 404
    
    def patch(self, id):
        data = request.get_json()

        # Query the database for the property with the given ID
        property = Property.query.get(id)

        if property:
           
            for key, value in data.items():
                if value is not None:
                    setattr(property, key, value)

            
            db.session.commit()

            
            success_message = f"Property with ID {id} has been successfully updated."

            return {
                'message': success_message,
                'id': property.id,
                'property_type': property.property_type,
                'property_category': property.property_category,
                'bedrooms': property.bedrooms,
                'bathrooms': property.bathrooms,
                'square_footage': property.square_footage,
                'media': property.media,
                'furnished': property.furnished,
                'description': property.description,
                'location_details': property.location_details,
                'landlord_name': property.landlord_name,
                'contact_phone': property.contact_phone,
                'contact_email': property.contact_email,
                'preferred_contact_method': property.preferred_contact_method,
                'additional_details': property.additional_details,
            }, 200
        else:
            return {'message': 'Property not found'}, 404
        
        
    def delete(self, id):
       
        property = Property.query.get(id)

        if property:
            
            db.session.delete(property)
            db.session.commit()
            return {'message': 'Property deleted successfully'}, 200
        else:
            return {'message': 'Property not found'}, 404
        


        





class ListingResource(Resource):
    @jwt_required()
    def get(self):
        listings = Listing.query.all()
        listing_list = [
            {
                'id': listing.id,
                'title': listing.title,
                'description': listing.description,
                'rent': listing.rent,
                'place': listing.place,
                'size': listing.size,
                'utilities': listing.utilities,
                'media': listing.media,
            }
            for listing in listings
        ]
        response= make_response( listing_list,200)
        return response
    
    
    
    # post method using flask.request
    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            title = data.get('title')
            description = data.get('description')
            rent = data.get('rent')
            place = data.get('place')
            size = data.get('size')
            utilities = data.get('utilities')
            media = data.get('media')

            # Create a new Listing object and add it to the database
            new_listing = Listing(
                title=title,
                description=description,
                rent=rent,
                place=place,
                size=size,
                utilities=utilities,
                media=media
            )
            db.session.add(new_listing)
            db.session.commit()

            # Prepare the success message
            success_message = f"Listing with ID {new_listing.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_listing.id,
                'title': new_listing.title,
                'description': new_listing.description,
                'rent': new_listing.rent,
                'place': new_listing.place,
                'size': new_listing.size,
                'utilities': new_listing.utilities,
                'media': new_listing.media
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400
 

class ListingResourceId(Resource):
    def get(self, id=None):
        if id is None:
            # If id is not provided, return all listings
            listings = Listing.query.all()
            listing_list = [
                {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
                for listing in listings
            ]
            return listing_list
        else:
            # If id is provided, return a specific listing by ID
            listing = Listing.query.get(id)
            if listing:
                return {
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }
            else:
                return {'message': 'Listing not found'}, 404

    

    def patch(self, id):
        data = request.get_json()
        if data:
            listing = Listing.query.get(id)
            if listing:
                # Update the listing attributes based on the provided data
                for key, value in data.items():
                    setattr(listing, key, value)

                # Commit changes to the database
                db.session.commit()

                # Prepare the success message
                success_message = f"Listing with ID {id} has been successfully updated."

                return {
                    'message': success_message,
                    'id': listing.id,
                    'title': listing.title,
                    'description': listing.description,
                    'rent': listing.rent,
                    'place': listing.place,
                    'size': listing.size,
                    'utilities': listing.utilities,
                    'media': listing.media,
                }, 200
            else:
                return {'message': 'Listing not found'}, 404
        else:
            return {'message': 'Invalid JSON data'}, 400  # 400 Bad Request status code

    def delete(self, id):
        listing = Listing.query.get(id)
        if listing:
            # Delete the listing from the database
            db.session.delete(listing)
            db.session.commit()
            return {'message': 'Listing deleted successfully'}, 200
        else:
            return {'message': 'Listing not found'}, 404

class LocationResource(Resource):
    def get(self):
        locations = Location.query.all()
        location_list = [
            # {
            #     'id': location.id,
            #     'city': location.city,
            #     'neighborhood': location.neighborhood,
            #     'specific_area': location.specific_area
            # }
            location.to_dict() for location in locations
        ]
        return location_list

class ReviewResource(Resource):
    def get(self):
        reviews = Review.query.all()
        review_list = [
            {
                'id': review.id,
                'user_id': review.user_id,
                'listing_id': review.listing_id,
                'property_id': review.property_id,
                'comment': review.comment,
                'review_date': review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }
            for review in reviews
        ]
        return review_list

   
    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            user_id = data.get('user_id')
            listing_id = data.get('listing_id')
            property_id = data.get('property_id')
            comment = data.get('comment')
            review_date_str = data.get('review_date')

            # Check if the required fields are present in the request
            if not all([user_id, listing_id, property_id, comment, review_date_str]):
                return {'message': 'All fields are required'}, 400

            try:
                # Parse the review_date_str into a Python datetime object
                review_date = datetime.strptime(review_date_str, '%Y-%m-%d ')
            except ValueError:
                return {'message': 'Invalid review_date format. Expected format: YYYY-MM-DD HH:MM:SS'}, 400

            # Create a new Review object and add it to the database
            new_review = Review(
                user_id=user_id,
                listing_id=listing_id,
                property_id=property_id,
                comment=comment,
                review_date=review_date
            )
            db.session.add(new_review)
            db.session.commit()

            # Prepare the success message
            success_message = f"Review with ID {new_review.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_review.id,
                'user_id': new_review.user_id,
                'listing_id': new_review.listing_id,
                'property_id': new_review.property_id,
                'comment': new_review.comment,
                'review_date': new_review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

        
class ReviewResourceId(Resource):
    def get(self, id):
        review = Review.query.get(id)
        if review:
            return {
                'id': review.id,
                'user_id': review.user_id,
                'listing_id': review.listing_id,
                'property_id': review.property_id,
                'comment': review.comment,
                'review_date': review.review_date.strftime('%Y-%m-%d %H:%M:%S')
            }, 200
        else:
            return {'message': 'Review not found'}, 404
        
    def patch(self, id):
        data = request.get_json()
        if data:
            review = Review.query.get(id)
            if review:
                # Update the review attributes based on the provided data
                if 'user_id' in data:
                    review.user_id = data['user_id']
                if 'listing_id' in data:
                    review.listing_id = data['listing_id']
                if 'property_id' in data:
                    review.property_id = data['property_id']
                if 'comment' in data:
                    review.comment = data['comment']
                if 'review_date' in data:
                    try:
                        review_date = datetime.strptime(data['review_date'], '%Y-%m-%d').date()
                    except ValueError:
                        return {'message': 'Invalid review_date format. Expected format: YYYY-MM-DD'}, 400
                    review.review_date = review_date
                # Commit changes to the database
                db.session.commit()

                # Prepare the success message
                success_message = f"Review with ID {id} has been successfully updated."

                return {
                    'message': success_message,
                    'id': review.id,
                    'user_id': review.user_id,
                    'listing_id': review.listing_id,
                    'property_id': review.property_id,
                    'comment': review.comment,
                    'review_date': review.review_date.strftime('%Y-%m-%d')
                }, 200
            else:
                return {'message': 'Review not found'}, 404
        else:
            return {'message': 'Invalid JSON data'}, 400

    def delete(self, id):
        review = Review.query.get(id)
        if review:
            # Delete the review from the database
            db.session.delete(review)
            db.session.commit()
            return {'message': 'Review deleted successfully'}, 200
        else:
            return {'message': 'Review not found'}, 404


class Favorite(Resource):
    def get(self):
        user_fav_properties = UserFavoriteProperty.query.all()
        user_fav_property_list = [
            {
                'id': fav_property.id,
                'user_id': fav_property.user_id,
                'listing_id': fav_property.listing_id,
                'property_id': fav_property.property_id,
            }
            for fav_property in user_fav_properties
        ]
        return user_fav_property_list

    def post(self):
        data = request.get_json()
        if data:
            # Extract data from the JSON payload
            user_id = data.get('user_id')
            listing_id = data.get('listing_id')
            property_id = data.get('property_id')

            # Create a new UserFavoriteProperty object and add it to the database
            new_user_fav_property = UserFavoriteProperty(
                user_id=user_id,
                listing_id=listing_id,
                property_id=property_id
            )
            db.session.add(new_user_fav_property)
            db.session.commit()

            # Prepare the success message
            success_message = f"UserFavoriteProperty with ID {new_user_fav_property.id} has been successfully created."

            return {
                'message': success_message,
                'id': new_user_fav_property.id,
                'user_id': new_user_fav_property.user_id,
                'listing_id': new_user_fav_property.listing_id,
                'property_id': new_user_fav_property.property_id,
            }, 201  # 201 Created status code
        else:
            return {'message': 'Invalid JSON data'}, 400

class FavoriteId(Resource):
    # def patch(self, id):
    #     data = request.get_json()
    #     if data:
    #         user_fav_property = UserFavoriteProperty.query.get(id)
    #         if user_fav_property:
    #             # Update the UserFavoriteProperty attributes based on the provided data
    #             if 'user_id' in data:
    #                 user_fav_property.user_id = data['user_id']
    #             if 'listing_id' in data:
    #                 user_fav_property.listing_id = data['listing_id']
    #             if 'property_id' in data:
    #                 user_fav_property.property_id = data['property_id']

    #             # Commit changes to the database
    #             db.session.commit()

    #             # Prepare the success message
    #             success_message = f"UserFavoriteProperty with ID {id} has been successfully updated."

    #             return {
    #                 'message': success_message,
    #                 'id': user_fav_property.id,
    #                 'user_id': user_fav_property.user_id,
    #                 'listing_id': user_fav_property.listing_id,
    #                 'property_id': user_fav_property.property_id,
    #             }, 200
    #         else:
    #             return {'message': 'UserFavoriteProperty not found'}, 404
    #     else:
    #         return {'message': 'Invalid JSON data'}, 400

    def delete(self, id):
        user_fav_property = UserFavoriteProperty.query.get(id)
        if user_fav_property:
            # Delete the UserFavoriteProperty from the database
            db.session.delete(user_fav_property)
            db.session.commit()
            return {'message': 'UserFavoriteProperty deleted successfully'}, 200
        else:
            return {'message': 'UserFavoriteProperty not found'}, 404





api.add_resource(UserResource, '/users')
api.add_resource(UserResourceId, '/users/<int:user_id>')
api.add_resource(LocationResource, '/locations')
api.add_resource(PropertyResource, '/properties')
api.add_resource(PropertyResourceId, '/properties/<int:id>')
api.add_resource(ListingResource, '/listings')
api.add_resource(ListingResourceId, '/listings/<int:id>')
api.add_resource(ReviewResource, '/reviews')
api.add_resource(ReviewResourceId,  '/reviews/<int:id>')
api.add_resource(Favorite, '/fav')
api.add_resource(FavoriteId, '/fav/<int:id>')



if __name__ == '__main__':
    app.run(port=5570,debug=True)