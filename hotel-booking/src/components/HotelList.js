import React, { useState, useEffect } from 'react';
import axios from 'axios';
import HotelCard from './HotelCard';

const HotelList = () => {
    const [hotels, setHotels] = useState([]);

    useEffect(() => {
        axios.get('/api/hotels/')
            .then(response => {
                setHotels(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the hotels!', error);
            });
    }, []);

    return (
        <div>
            <h1>Hotels</h1>
            <div className="hotel-list">
                {hotels.map(hotel => (
                    <HotelCard key={hotel.id} hotel={hotel} />
                ))}
            </div>
        </div>
    );
};

export default HotelList;
