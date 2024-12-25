import React from "react";
import ExerciseCard from './ExerciseCard'

// Render the list of exercises and delegates the display of indivdual exercise details
// to another component

function ExerciseList({exercises}) {
    return (
        <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
            {exercises.map((exercise) => (
                <ExerciseCard key={exercise.id} item={exercise} />
            ))}
        </div>
    )
}

export default ExerciseList