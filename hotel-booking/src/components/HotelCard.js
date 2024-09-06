import React, { useState } from 'react';
import axios from 'axios';

const HotelCard = ({ hotel }) => {
    const [bookingCount, setBookingCount] = useState(hotel.completed_bookings);

    const handleVisit = () => {
        axios.post(`/api/hotels/${hotel.id}/visit/`, { user_id: 1 })  // Replace user_id with actual user ID
            .then(response => {
                console.log('Hotel visited:', response.data);
            })
            .catch(error => {
                console.error('There was an error visiting the hotel!', error);
            });
    };

    const handleBooking = () => {
        axios.post('http://127.0.0.1:8000/api/bookings/', {
            user_id: 1,  // Replace with actual user ID
            hotel_id: hotel.id,
            status: 'completed'  // Setting status as completed to increment the count
        })
        .then(response => {
            setBookingCount(prevCount => prevCount + 1); // Increment the booking count
            alert(`Booking successful! Total bookings: ${bookingCount + 1}`);
        })
        .catch(error => {
            console.error('There was an error creating the booking!', error);
        });
    };

    return (
        <div className="hotel-card">
            <img src={hotel.image_url} alt={hotel.name} />
            <h2>{hotel.name}</h2>
            <p>Rating: {hotel.ratings}</p>
            <p>{hotel.description}</p>
            <button onClick={handleVisit}>Visit</button>
            <button onClick={handleBooking}>Book Now</button>
        </div>
    );
};

export default HotelCard;
