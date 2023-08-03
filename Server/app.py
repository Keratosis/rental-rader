#imports
from flask import Flask, make_response,request
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort
from datetime import datetime
from models import db,User, Listing, Location, Property, RentalTerms, Review, UserFavoriteProperty 
from flask_cors import CORS

# initiasing app
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '332nsdbd993h3bd84920'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate =Migrate(app,db) 
db.init_app(app)
api = Api(app)


@app.route("/") 
@app.route("/home")
def home_page():
    return '<h1>Home</h1>'

class UserResource(Resource):
    def get(self):
        user_list = [{'id': user.id, 
                      'name': user.username,
                      'email': user.email, 
                      'role': user.role
                      } 
                     for user in User.query.all()]
        # user_list1= [ user.to_dict() for user in User.query.all()]
        responce = make_response(
                                user_list,
                                20)      
        return responce


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
        # Parse the request data for updating the property
        
        # Get the JSON data from the request
        data = request.get_json()

        # Query the database for the property with the given ID
        property = Property.query.get(id)

        if property:
            # Update the property attributes based on the provided data
            for key, value in data.items():
                if value is not None:
                    setattr(property, key, value)

            # Commit changes to the database
            db.session.commit()

            # Prepare the success message
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
        # Query the database for the property with the given ID
        property = Property.query.get(id)

        if property:
            # Delete the property from the database
            db.session.delete(property)
            db.session.commit()
            return {'message': 'Property deleted successfully'}, 200
        else:
            return {'message': 'Property not found'}, 404
        


        





class ListingResource(Resource):
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