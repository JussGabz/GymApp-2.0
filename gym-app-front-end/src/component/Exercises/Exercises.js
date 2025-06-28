import React, { useEffect, useState } from "react";
import Error from "../Error";
import { fetchExercises } from "../../services/exerciseService";
import ExerciseSearchBar from "./ExerciseSearch";
import ExerciseCard from "./ExerciseCard";
import { EXERCISES_ENDPOINT } from "../../config/apiConfig";

//Main Exercise Component -> Render the Headder
// Fetch the Data using useFetchExercises
// Conditionally Rendering Skeleton Loader, Error or Exercise List

function Exercises() {
    // const { data, loading, error } = useFetchExercises();

    const [ searchQuery, setSearchQuery] = useState('')
    const [ data, setData ] = useState(null)
    const [nextUrl, setNextUrl] = useState(null)
    const [previousUrl, setPreviousUrl] = useState(null)
    const [currentUrl, setCurrentUrl] = useState(EXERCISES_ENDPOINT)

    // if (loading) return <SkeletonLoader />
    // if (error) return <Error message={error} />

    useEffect(() => {
        fetchData(currentUrl)
    }, [currentUrl])

    const fetchData = async (url) => {
        try {
            const response = await fetchExercises(url)
            console.log(response)
            setData(response)
            setNextUrl(response.next)
            setPreviousUrl(response.previous)

        } catch (error) {
            console.error('Error fetching exercise data:', error)
        } finally {
        }
    }

    const handleSearch = (query) => {
        setSearchQuery(query)
        setCurrentUrl(`${EXERCISES_ENDPOINT}?name=${encodeURIComponent(query)}`)
    }

    return (
        <div className="container">
            <div style={{ margin: '2rem' }}>
                <h1 style={{ textAlign: 'center' }}>Exercises</h1>
            </div>
            <div>
                <ExerciseSearchBar onSearch={handleSearch} />
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

export default Exercises