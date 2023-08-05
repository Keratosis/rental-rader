from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
 
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    hashed_password = db.Column(db.String)
    role = db.Column(db.String)
    registration_date = db.Column(db.DateTime, server_default=db.func.now())

    #relationship
    properties = relationship('Property', backref='property_owner')
    reviews = relationship('Review', backref='user_reviews', overlaps="reviewer,userx")
    favorite_properties = relationship('UserFavoriteProperty', backref='user')

    serialize_rules = ('-properties.user', '-favorite_properties.user', '-reviews.user',)


    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"

class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, ForeignKey('location.id'))
    country = db.Column(db.String)  
    city_town = db.Column(db.String)  
    neighborhood_area = db.Column(db.String)
    address = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    property_type = db.Column(db.String)
    property_category = db.Column(db.String)
    property_rent = db.Column(db.Float, default=0.0)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    square_footage = db.Column(db.Integer)
    furnished = db.Column(db.String, default='Y')
    description = db.Column(db.String)
    location_details = db.Column(db.String)
    property_owner_name = db.Column(db.String)
    property_owner_photo = db.Column(db.String)
    contact_phone = db.Column(db.String)
    contact_email = db.Column(db.String)
    contact_whatsapp = db.Column(db.String)
    preferred_contact_method = db.Column(db.String)
    additional_details = db.Column(db.String)

    # Media fields
    main_image = db.Column(db.String)
    images = db.Column(db.String)
    house_tour_video = db.Column(db.String)
    property_documents = db.Column(db.String)

    # Social media accounts
    facebook = db.Column(db.String)
    twitter = db.Column(db.String)
    instagram = db.Column(db.String)
    linkedin = db.Column(db.String)
    other_social_media = db.Column(db.String)

    # Amenities field
    amenities = db.Column(db.String)


    #relationship
    rental_terms = relationship('RentalTerms', backref='property')
    # userz = db.relationship('User', backref='properties')
    
    
    serialize_rules = ('-user.properties',)

    def __repr__(self):
        return f"<Property(id={self.id}, property_type='{self.property_type}', bedrooms={self.bedrooms}, bathrooms={self.bathrooms})>"

class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, ForeignKey('location.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)
    rent = db.Column(db.String)
    place = db.Column(db.String)
    size = db.Column(db.String)
    utilities = db.Column(db.String)
    media = db.Column(db.String)
    
    # Relationships
    reviewws = relationship('Review', backref='listingz')

    
    def __repr__(self):
        return f"<Listing(id={self.id}, title='{self.title}', renta={self.rent}, location='{self.location}')>"

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, ForeignKey('listing.id'))
    property_id = db.Column(db.Integer, ForeignKey('properties.id'))
    comment = db.Column(db.String)
    review_date = db.db.Column(db.DateTime, server_default =db.func.now())
    
    #relationship
    user = db.relationship('User', back_populates='reviews', overlaps="reviewer,userx")
    listing = relationship('Listing', backref='review')
    properties = relationship('Property', backref='review')
    
    


    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, listing_id={self.listing_id}, property_id={self.property_id})>"

class UserFavoriteProperty(db.Model):
    __tablename__ = 'user_favorite_property'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, ForeignKey('listing.id'))
    property_id = db.Column(db.Integer, ForeignKey('properties.id'))
    
    # Relationships
    usery = db.relationship('User', backref='favorite_propertiesx')
    listing = relationship('Listing', backref='favorite_properties')
    property = relationship('Property', backref='favorite_properties')

    def __repr__(self):
        return f"<UserFavoriteProperty(id={self.id}, user_id={self.user_id}, listing_id={self.listing_id}, property_id={self.property_id})>"  


class Location(db.Model,SerializerMixin):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    neighborhood = db.Column(db.String)
    specific_area = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)

    properties = relationship('Property', backref='location')
    listings = relationship('Listing', backref='location')
    
    serialize_rules = ('-properties.location',)
    def __repr__(self):
        return f"<Location(id={self.id}, city='{self.city}', neighborhood='{self.neighborhood}', specific_area='{self.specific_area}')>"

class RentalTerms(db.Model):
    __tablename__ = 'rental_terms'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, ForeignKey('properties.id'))
    rental_price = db.Column(db.Integer)
    security_deposit = db.Column(db.Integer)
    lease_duration_min = db.Column(db.Integer)
    lease_duration_max = db.Column(db.Integer)
    additional_fees = db.Column(db.String)

    

    def __repr__(self):
        return f"<RentalTerms(id={self.id}, rental_price={self.rental_price}, security_deposit={self.security_deposit})>"