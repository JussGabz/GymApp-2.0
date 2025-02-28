import React, { useEffect, useState } from "react";
import useFetchExercises from "../../hooks/useFetchexercises";
import SkeletonLoader from "../SkeletonLoader";
import Error from "../Error";
import ExerciseList from "./ExerciseList";
import { fetchExercises } from "../../services/exerciseService";
import ExerciseSearchBar from "./ExerciseSearch";
import WorkoutCard from "../workoutcard";
import ExerciseCard from "./ExerciseCard";

//Main Exercise Component -> Render the Headder
// Fetch the Data using useFetchExercises
// Conditionally Rendering Skeleton Loader, Error or Exercise List

function Exercises() {
    // const { data, loading, error } = useFetchExercises();

    const [ searchQuery, setSearchQuery] = useState('')
    const [ data, setData ] = useState(null)

    // if (loading) return <SkeletonLoader />
    // if (error) return <Error message={error} />

    useEffect(() => {
        fetchData(searchQuery)
    }, [searchQuery])

    const fetchData = async () => {
        try {
            const response = await fetchExercises(searchQuery)
            // console.log(response)
            setData(response)
            if (!response.ok) throw new Error('Failed to fetch data')
            const jsonData = await response.json()
            console.log(jsonData)
            setData(jsonData)
            
        } catch (error) {
            console.error('Error fetching exercise data:', error)
        } finally {
        }
    }
    return (
        <div className="container">
            <div style={{ margin: '2rem' }}>
                <h1 style={{ textAlign: 'center' }}>Exercises</h1>
            </div>
            <div>
                <ExerciseSearchBar onSearch={setSearchQuery} />
            </div>
            { data ? (
                <div className="row rows-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
                    {data.results.map((item) => (
                        <ExerciseCard key={item.id} exercise={item} />
                    ))
                    }
                </div>
            ) : (
                <div> No Data Available </div>
            )}
        </div>
    )
}

export default Exercises