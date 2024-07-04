import React, { useState, useEffect } from 'react';

function Exercise() {

    // State to hold the fetched data
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
            // Fetch data from your Django endpoint (e.g., list action of your ViewSet)
            const response = await fetch('http://127.0.0.1:8000/exercises/');
            
            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            
            // Parse the JSON response
            const jsonData = await response.json();
            
            // Update the component state with the fetched data
            setData(jsonData);
            } catch (error) {
            console.error('Error fetching data:', error);
            }
        };
    
        // Call the fetchData function when the component mounts
        fetchData();
        }, []); // Empty dependency array ensures the effect runs only once
        
    return (
        <div className="container">
            <div style={{ margin: "2rem"}}>
                <h1 style={{ textAlign: 'center'}}>Exercises</h1>
            </div>
            <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                {data ? (
                    data.results.map((item) => (
                        <div key={item.id} className="col">
                            <div className="card h-100">
                                <img src="images/juss-gym-logo.png" className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h5 className="card-title">Exercise Name: {item.name}</h5>
                                    <h6 className="card-title">Target Area: {item.name}</h6>
                                </div>
                            </div>
                        </div>
                    ))
                ) : (
                    <div>No data available</div>
                )}
            </div>
        </div>
    )
}

export default function Exercises(){
    return (
    <Exercise />
    )
}