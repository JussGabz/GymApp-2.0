import React from "react";
import WorkoutPlanCard from "./WorkoutPlanCard";

//Render the List of workout plans and delegates the display of individual workout plan details
// to another component

function WorkoutPlanList({ workoutplans }) {
    return (
        <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
            {workoutplans.map((workoutplan) => (
                <WorkoutPlanCard key={workoutplan.id} item={workoutplan} />
            ))}
        </div>
    )
}

export default WorkoutPlanList