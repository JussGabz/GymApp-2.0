import React, { useState, useEffect } from 'react';
import SearchBar from './searchbar';
import WorkoutCard from './WorkoutPlans/WorkoutPlanCard';
import WorkoutDropDown from './workoutFilter';

// Main Component
const WorkoutPlan = () => {
    const [data, setData] = useState(null)
    const [searchQuery, setSearchQuery] = useState('')
    const [isLoading, setIsLoading] = useState(false)

    useEffect(() => {
        fetchData(searchQuery);
    }, [searchQuery])

    const fetchData = async (query = '') => {
        setIsLoading(true)
        const token = localStorage.getItem('access_token')
        let url = `http://127.0.0.1:8000/workoutplans/${query ? `?name=${query}` : ''}`
        console.log(url)

        try {
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            if (!response.ok) throw new Error('Failed to fetch data')
            const jsonData = await response.json();
            setData(jsonData)
        } catch (error) {
            console.error('Error fetching data:', error)
        } finally {
            setIsLoading(false)
        }
    }

    return (
        <div className='container'>
            <div style={{ margin: "2rem" }}>
                <h1 style={{ textAlign: 'center' }}>Work Out Plans</h1>
            </div>
            <div className='row'>
                {/* Search Bar */}
                <div className='col-md-4'>
                    <SearchBar onSearch={(query) => setSearchQuery(query)} />
                </div>
                {/* Workout Filter */}
                <div className='col-md-4'>
                    <WorkoutDropDown />
                </div>
                <div className='col-md-4'>
                    <input
                        type='text'
                        className='form-control mb-3'
                        placeholder='Another filter'
                    />
                </div>
            </div>

            {/* Loading State */}
            {isLoading ? <div> Loading... </div> : (
                <div className='row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4'>
                    {data && data.results.length > 0 ? (
                        data.results.map((item) => (
                            <WorkoutCard key={item.id} workout={item} />
                        ))
                    ) : (
                        <div> No Data available </div>
                    )}
                </div>
            )}
        </div>
    )
}

export default function WorkoutPlans() {
    return <WorkoutPlan />
}