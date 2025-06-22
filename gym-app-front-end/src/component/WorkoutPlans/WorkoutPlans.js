import React, { useEffect, useState } from "react";
import Error from "../Error";
import WorkoutPlanSearchBar from "./WorkoutPlanSearch";
import WorkoutCard from "./WorkoutPlanCard";
import { fetchWorkoutPlans } from "../../services/workoutplanService";
import { Button } from "react-bootstrap";
import { WORKOUT_PLANS_ENDPOINT } from "../../config/apiConfig"


// Main Workout Plan Component -> Render the Header
// Fetch the Data using useFetchWorkoutPlans
// COnditionally Rendering Skeleton Loader

function WorkoutPlans() {
    // const { data, loading, error } = useFetchWorkoutPlans();

    // Set variables for user search query & data from api
    const [ searchQuery, setSearchQuery] = useState('')
    const [items, setItems] = useState(null)
    const [nextUrl, setNextUrl] = useState(null)
    const [previousUrl, setPreviousUrl] = useState(null)
    const [currentUrl, setCurrentUrl] = useState(WORKOUT_PLANS_ENDPOINT)

    // if (loading) return <SkeletonLoader />
    // if (error) return <Error message={error} />

    useEffect(() => {
        fetchData(currentUrl)
        // .then(res => res.json())
        // .then(data => {
        //     setItems(data.results)
        //     setNextUrl(data.next)
        //     setPreviousUrl(data.previous)
        // }
    // )
    }, [currentUrl])

    const fetchData = async (url) => {
        try {
            const jsonData = await fetchWorkoutPlans(url)
            console.log(jsonData)
            setItems(jsonData.results)
            setNextUrl(jsonData.next)
            setPreviousUrl(jsonData.previous)
            
        } catch (error) {
            console.error('Error fetching data:', error)
        } finally {
 
        }
    }

    const handleSearch = (query) => {
        setSearchQuery(query)
        setCurrentUrl(`${WORKOUT_PLANS_ENDPOINT}?name=${encodeURIComponent(query)}`)
    }

    return (
        <div className="container">
            <div style={{ margin: '2rem' }}>
                <h1 style={{ textAlign: "center" }}>Workout Plans</h1>
            </div>
            <div>
                <WorkoutPlanSearchBar onSearch={handleSearch}/>    
            </div>
            <div>
                <Button variant="primary" href="/addworkoutplan"> Add New Workout Plan</Button>
            </div>
            {/* {data ? <WorkoutPlanList workoutplans={data.results} /> : <div>No Data Available</div>} */}
            { items ? (
            <div className="row rows-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                {items.map((item) => (
                    <WorkoutCard key={item.id} workout={item} />
                ))
                }
            </div>
            ) : (
                <div>No Data Available</div>
            )}

            <div style={{ marginTop: '1rem' }}>
                <button
                    onClick={() => setCurrentUrl(previousUrl)}
                    disabled={!previousUrl}
                >
                    Previous
                </button>
                <button
                    onClick={() => setCurrentUrl(nextUrl)}
                    disabled={!nextUrl}
                >
                    Next
                </button>
            </div>
        </div>
        
    )
}

export default WorkoutPlans