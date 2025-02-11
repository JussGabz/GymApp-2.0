import React, { useEffect, useState } from "react";
import useFetchWorkoutPlans from "../../hooks/useFetchWorkoutPlans";
import SkeletonLoader from "../SkeletonLoader";
import Error from "../Error";
import WorkoutPlanList from "./WorkoutPlanList";
import WorkoutPlanSearchBar from "./WorkoutPlanSearch";
import WorkoutCard from "../workoutcard";
import { getToken } from "../../utils/tokenUtils";

// Main Workout Plan Component -> Render the Header
// Fetch the Data using useFetchWorkoutPlans
// COnditionally Rendering Skeleton Loader

function WorkoutPlans() {
    // const { data, loading, error } = useFetchWorkoutPlans();
    const [ searchQuery, setSearchQuery] = useState('')
    const [data, setData] = useState(null)

    // if (loading) return <SkeletonLoader />
    // if (error) return <Error message={error} />

    useEffect(() => {
        fetchData(searchQuery);
    }, [searchQuery])

    const fetchData = async (query = '') => {
        const token = getToken()
        let url = `http://127.0.0.1:8000/workoutplans/${query ? `?name=${query}` : ''}`
        try {
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                }
            })
            if (!response.ok) throw new Error('Failed to fetch data')
            const jsonData = await response.json()
            setData(jsonData)
        } catch (error) {
            console.error('Error fetrching data:', error)
        } finally {

        }
    }
    return (
        <div className="container">
            <div style={{ margin: '2rem' }}>
                <h1 style={{ textAlign: "center" }}>Workout Plans</h1>
            </div>
            <div>
                <WorkoutPlanSearchBar onSearch={(query) => setSearchQuery(query)}/>    
            </div>
            {data ? <WorkoutPlanList workoutplans={data.results} /> : <div>No Data Available</div>}
            <div className="row rows-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                {data.result.map((item) => (
                    <WorkoutCard key={item.id} workout={item} />
                ))
                }
            </div>
        </div>
    )
}

export default WorkoutPlans