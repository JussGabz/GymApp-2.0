import React from "react";

// function ExerciseCard({ item }) {
//     return (
//         <div className="col">
//             <div className="card h-100">
//                 <img src="images/juss-gym-logo.png" className="card-img-top" alt="Exercise" />
//                 <div className="card-body">
//                     <h5 className="card-title">Exercise Name: {item.name}</h5>
//                     <h6 className="card-title">Target Area: {item.target_area}</h6>
//                 </div>
//             </div>
//         </div>
//     )
// }

const ExerciseCard = ({ exercise }) => (
    <div className="col">
        <div className="card h-100">
            <img src="images/juss-gym-logo.png" className="card-img-top" alt="Exercise" />
            <div className="card-body">
                <h5 className="card-title">Exercise Name: {exercise.name}</h5>
                <h6 className="card-title">Target Area: {exercise.target_area}</h6>
            </div>
        </div>
    </div>
)

export default ExerciseCard