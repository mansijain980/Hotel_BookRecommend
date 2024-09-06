
import './App.css';

import React from 'react';
import HotelList from './components/HotelList';
import RecentActivities from './components/RecentActivities';

function App() {
    return (
        <div className="App">
            <HotelList />
            <RecentActivities />
        </div>
    );
}

export default App;
