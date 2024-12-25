import React from "react";

function WorkoutPlanCard({ item }) {
    return (
        <div className="col">
            <div className="card h-100">
                <img src="images/juss-gym-logo.png" className="card-img-top" alt="WorkoutPlan" />
                <div className="card-body">
                    <h5 className="card-title">Workout Plan: {item.name}</h5>
                    <p className="card-text"><small className="text-muted">Date Added: {item.date_added}</small></p>
                    <p className="card-text"><small className="text-muted">Created By: {item.created_by}</small></p>
                </div>
            </div>
        </div>
    )
}

export default WorkoutPlanCard