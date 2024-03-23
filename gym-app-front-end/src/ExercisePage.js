import React, { useState, useEffect } from 'react';
import Menu from './Menu';

const ExercisePage = () => {
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
      <div>
        < Menu />
        <h1>Exercises</h1>
        <p>Latest Exercises</p>
        {data ? (
            <ul>
                {data.results.map(item => (
                    <li key={item.id}>{item.name}</li>
                ))}
            </ul>
        ) : (
            <p>Loading...</p>
        )}
        {/* Add more content as needed */}
      </div>
    );
  };
  
  export default ExercisePage;