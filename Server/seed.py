from app import app
from models import User, Listing, Location, Property, RentalTerms,  Review, UserFavoriteProperty, db

# Function to seed the database with sample data
def seed_data():
    # Clear the existing data from all tables
    User.query.delete()
    Listing.query.delete()
    Location.query.delete()
    Property.query.delete()
    RentalTerms.query.delete()
    Review.query.delete()
    UserFavoriteProperty.query.delete()

    # Seed data for users
    user1 = User(username='braxton', email='braxton@example.com', hashed_password='123456', role='tenant')
    user2 = User(username='shaffie', email='shaffie@example.com', hashed_password='123456', role='landlord')

    db.session.add_all([user1, user2])
    db.session.commit()

    # Seed data for locations
    location1 = Location(city='mombasa', neighborhood='Neighborhood A', specific_area='Area A', latitude='0.000', longitude='0.000')
    location2 = Location(city='', neighborhood='Neighborhood B', specific_area='Area B', latitude='0.000', longitude='0.000')

    db.session.add_all([location1, location2])
    db.session.commit()
    
    
     # Seed data for listings
    listing_data = [
        {
            'id': 1,
            'location_id': 1,
            'title': 'Spacious Downtown Office Suite',
            'description': 'A modern and spacious office suite located in the heart of downtown. It features large windows for ample natural light, a reception area, three private offices, a conference room, and a break area. Perfect for a growing business.',
            'rent': '$3,400/month',
            'place': '4404 Brian Plains, Port Marie, IN 70903',
            'size': '1000 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2013/09/14/19/53/city-182223_640.jpg'
        },
        {
            'id': 2,
            'location_id': 2,
            'title': 'Cozy Studio Apartment near the Park',
            'description': 'This charming studio apartment is just a short walk from the local park. It offers an open floor plan with a fully equipped kitchen, a comfortable living area, and a separate sleeping area. Ideal for a single professional or student.',
            'rent': '$3,000/month',
            'place': '456 Elm Avenue, Parkside',
            'size': '500 sqft',
            'utilities': 'High-speed WiFi, parking space, security (CCTV)',
            'media': 'https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg'
        },
         {
        'id': 3,
        'title': 'Prime Retail Space on Main Street',
        'location_id': 3,
        'description': 'An excellent opportunity to lease a prime retail space on Main Street. The property features a spacious layout, large display windows, and high foot traffic. Ideal for a boutique, cafe, or specialty shop.',
        'rent': '$5,200/month',
        'place': '789 Main Street, Downtown',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/08/25/11/50/shopping-mall-906721_640.jpg',
        'utilities': 'WiFi, parking space'
        },
        {
        'id': 4,
        'title': 'Luxury Penthouse with Stunning Views',
        'location_id': 4,
        'description': 'Experience luxury living in this exquisite penthouse apartment boasting breathtaking views of the city skyline. It offers high-end finishes, a gourmet kitchen, a private terrace, and access to exclusive amenities such as a fitness center and pool.',
        'rent': '$8,500/month',
        'place': '10 Highrise Avenue, Skyview Heights',
        'size': '2,800 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/06/21/20/16/real-estate-374107_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
         },
    {
        'id': 5,
        'title': 'Industrial Warehouse with Loading Dock',
        'location_id': 1,
        'description': 'This spacious industrial warehouse is equipped with a loading dock, high ceilings, and ample storage space. It\'s perfect for businesses requiring logistics support or additional inventory space.',
        'rent': '$4,000/month',
        'place': '111 Warehouse Lane, Industrial District',
        'size': '5,000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/12/09/17/57/hall-3865370_1280.jpg',
        'utilities': 'Parking space, security (guardmen), back-up power'
    },
    {
        'id': 6,
        'title': 'Stylish 2-Bedroom Apartment in Trendy Neighborhood',
        'location_id': 5,
        'description': 'Embrace the vibrant city life in this stylish 2-bedroom apartment situated in a trendy neighborhood. It features a modern kitchen, spacious living area, and access to nearby restaurants, shops, and entertainment options.',
        'rent': '$1,000/month',
        'place': '222 Oak Street, Trendyville',
        'size': '900 square feet',
        'media': 'https://cdn.pixabay.com/photo/2014/07/31/21/41/apartment-406901_640.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 7,
        'title': 'Commercial Office Space with Flexible Layout',
        'location_id': 3,
        'description': 'This versatile commercial office space offers a flexible layout that can be customized to suit your business needs. It includes private offices, open work areas, a conference room, and a reception area. Conveniently located near major highways.',
        'rent': '$4,500/month',
        'place': '333 Business Boulevard, Business District',
        'size': '3500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2015/11/15/20/49/modern-office-1044807_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 8,
        'title': 'Quaint Cottage with Private Garden',
        'location_id': 2,
        'description': 'Escape to this charming cottage nestled in a serene neighborhood. It boasts a private garden, a cozy living area, a fully equipped kitchen, and two comfortable bedrooms. A perfect retreat for nature lovers.',
        'rent': '$1,800/month',
        'place': '252 Mark Plains, Dennisberg, IN 51233',
        'size': '1200 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/08/15/00/45/log-cabin-1594361_1280.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    },
    {
        'id': 9,
        'title': 'Retail Space in Busy Shopping Plaza',
        'location_id': 2,
        'description': 'Take advantage of this prime retail space located in a bustling shopping plaza. With high visibility and a steady flow of customers, it presents an excellent opportunity for your business to thrive.',
        'rent': '$3,800/month',
        'place': '555 Plaza Avenue, Shopper\'s Paradise',
        'size': '1000 sqft',
        'media': 'https://cdn.pixabay.com/photo/2018/10/15/14/58/cape-town-3749167_1280.jpg',
        'utilities': 'WiFi, parking space'
    },
    {
        'id': 10,
        'title': 'Modern Office Suite with River View',
        'location_id': 1,
        'description': 'Enjoy panoramic river views from this modern office suite. It offers a professional environment with a reception area, private offices, a conference room, and a break area. Conveniently located near downtown amenities.',
        'rent': '$3,800/month',
        'place': '666 Riverside Drive, Riverview Center',
        'size': '1500 sqft',
        'media': 'https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg',
        'utilities': 'WiFi, parking space, security (CCTV), back-up power'
    }
      
    ]

    for listing in listing_data:
        new_listing = Listing(
            id=listing['id'],
            location_id=listing['location_id'],
            title=listing['title'],
            description=listing['description'],
            rent=listing['rent'],
            place=listing['place'],
            size=listing['size'],
            utilities=listing['utilities'],
            media=listing['media']
        )
        db.session.add(new_listing)

    db.session.commit()
    # Seed data for properties
    property1 = Property(
        location_id=location1.id,
        user_id=user1.id,
        property_type='Office',
        property_category='Commercial',
        media = 'https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg',
        bedrooms=None,
        bathrooms=None,
        square_footage=1000,
        description='A modern and spacious office suite located in the heart of downtown. It features large windows for ample natural light, a reception area, three private offices, a conference room, and a break area. Perfect for a growing business.',
        location_details='Near public transportation',
        landlord_name='John Doe',
        contact_phone='123-456-7890',
        contact_email='john.doe@example.com',
        preferred_contact_method='Phone',
        additional_details='No smoking allowed.'
    )
    property2 = Property(
        location_id=location2.id,
        user_id=user2.id,
        property_type='Apartment',
        property_category='Residential',
        media = 'https://cdn.pixabay.com/photo/2016/10/16/10/30/office-space-1744803_640.jpg',
        bedrooms=None,
        bathrooms=None,
        square_footage=500,
        description='This charming studio apartment is just a short walk from the local park. It offers an open floor plan with a fully equipped kitchen, a comfortable living area, and a separate sleeping area. Ideal for a single professional or student.',
        location_details='Near parks and public amenities',
        landlord_name='Jane Smith',
        contact_phone='987-654-3210',
        contact_email='jane.smith@example.com',
        preferred_contact_method='Email',
        additional_details='Pets allowed with additional deposit.'
    )

    db.session.add_all([property1, property2])
    db.session.commit()
    # Seed data for rental terms
    rental_terms1 = RentalTerms(
        property_id=property1.id,
        rental_price=3500,
        security_deposit=1000,
        lease_duration_min=12,
        lease_duration_max=24,
        additional_fees='None'
    )
    rental_terms2 = RentalTerms(
        property_id=property2.id,
        rental_price=1200,
        security_deposit=800,
        lease_duration_min=6,
        lease_duration_max=12,
        additional_fees='Utilities not included'
    )

    db.session.add_all([rental_terms1, rental_terms2])
    db.session.commit()


    # Seed data for reviews
    review1 = Review(user_id=user1.id, listing_id=None, property_id=property1.id, comment='Great office space!')
    review2 = Review(user_id=user2.id, listing_id=None, property_id=property2.id, comment='Cozy apartment with a lovely view.')

    db.session.add_all([review1, review2])
    db.session.commit()

    # Seed data for user favorite properties
    user_favorite_property1 = UserFavoriteProperty(user_id=user1.id, listing_id=None, property_id=property2.id)
    user_favorite_property2 = UserFavoriteProperty(user_id=user2.id, listing_id=None, property_id=property1.id)

    db.session.add_all([user_favorite_property1, user_favorite_property2])
    db.session.commit()

# Run the seed function
if __name__ == '__main__':
    with app.app_context():
        seed_data()
