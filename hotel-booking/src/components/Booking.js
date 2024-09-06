import React, { useState } from 'react';
import axios from 'axios';

const Booking = ({ hotel }) => {
    const [status, setStatus] = useState('draft');

    const handleBooking = () => {
        axios.post('/api/bookings/', {
            user_id: 1,  // Replace with actual user ID
            hotel_id: hotel.id,
            status: status
        })
            .then(response => {
                console.log('Booking completed:', response.data);
            })
            .catch(error => {
                console.error('There was an error completing the booking!', error);
            });
    };

    return (
        <div>
            <h2>Book {hotel.name}</h2>
            <select value={status} onChange={(e) => setStatus(e.target.value)}>
                <option value="draft">Draft</option>
                <option value="completed">Completed</option>
            </select>
            <button onClick={handleBooking}>Submit Booking</button>
        </div>
    );
};

export default Booking;
