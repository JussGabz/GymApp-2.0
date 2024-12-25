import React from "react";
import useFetchExercises from "../../hooks/useFetchexercises";
import SkeletonLoader from "../SkeletonLoader";
import Error from "../Error";
import ExerciseList from "./ExerciseList";

//Main Exercise Component -> Render the Headder
// Fetch the Data using useFetchExercises
// Conditionally Rendering Skeleton Loader, Error or Exercise List

function Exercises() {
    const { data, loading, error } = useFetchExercises();

    if (loading) return <SkeletonLoader />
    if (error) return <Error message={error} />

    return (
        <div className="container">
            <div style={{ margin: '2rem' }}>
                <h1 style={{ textAlign: 'center' }}>Exercises</h1>
            </div>
            {data ? <ExerciseList exercises={data.results} /> : <div>No Data Available</div>}
        </div>
    )
}

export default Exercises