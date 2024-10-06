import React, { useState, useEffect } from 'react';

// Re-usable SearchBar Component
const SearchBar = ({ onSearch }) => (
    <form onSubmit={(e) => { e.preventDefault(); onSearch(); }}>
        <div className='input-group mb-3'>
            <input
                type='text'
                className='form-control'
                placeholder='Search workout plans'
                onChange={(e) => onSearch(e.target.value)}
            />
            <button className='btn btn-outline-secondary' type='submit'>Search</button>
        </div>
    </form>
)

// Reusable WorkoutCard Component
const WorkoutCard = ({ workout }) => (
    <div className='col'>
        <div className='card h-100'>
            <img src='images/juss-gym-logo.png' className='card-img-top' alt='...' />
            <div className='card-body'>
                <h5 className='card-title'>Workout Plan: {workout.name}</h5>
                {workout.exercises.map(exercise => (
                    <p key={exercise.id} className='card-text'>{exercise.name}</p>
                ))}
                <p className='card-text'><small className='text-muted'>Date Added: {workout.date_added}</small></p>
                <p className='card-text'><small className='text-muted'>Created By: {workout.created_by}</small></p>
            </div>
        </div>
    </div>
);

// Main Component
const WorkoutPlan = () => {
    const [data, setData] = useState(null)
    const [searchQuery, setSearchQuery] = useState('')
    const [isLoading, setIsLoading] = useState(false)

    useEffect(() => {
        fetchData();
    }, [searchQuery])

    const fetchData = async (query = '') => {
        setIsLoading(true)
        const token = localStorage.getItem('access_token')
        let url = `http://127.0.0.1:8000/workoutplans/${query ? `?search=${query}` : ''}`

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

            {/* Search Bar */}
            <SearchBar onSearch={(query) => setSearchQuery(query)} />

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