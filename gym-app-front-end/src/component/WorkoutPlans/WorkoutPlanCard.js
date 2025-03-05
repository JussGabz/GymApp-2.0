// Reusable WorkoutCard Component
const WorkoutCard = ({ workout }) => (
    <div className='col'>
        <div className='card h-100'>
            <img src='images/juss-gym-logo.png' className='card-img-top' alt='...' />
            <div className='card-body'>
                <h5 className='card-title'>Workout Plans: {workout.name}</h5>
                {workout.exercises.map(exercise => (
                    <p key={exercise.id} className='card-text'>{exercise.name}</p>
                ))}
                <p className='card-text'><small className='text-muted'>Date Added: {workout.date_added}</small></p>
                <p className='card-text'><small className='text-muted'>Created By: {workout.created_by}</small></p>
            </div>
        </div>
    </div>
);

export default WorkoutCard