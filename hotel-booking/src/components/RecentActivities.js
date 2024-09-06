import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RecentActivities = () => {
    const [activities, setActivities] = useState([]);

    useEffect(() => {
        axios.get('/api/activities/recent/')
            .then(response => {
                setActivities(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the activities!', error);
            });
    }, []);

    return (
        <div>
            <h2>Recent Activities</h2>
            <ul>
                {activities.map(activity => (
                    <li key={activity.id}>
                        {activity.user.username} {activity.activity_type} {activity.hotel.name} at {new Date(activity.timestamp).toLocaleString()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RecentActivities;
