// import WorkoutPlans from './component/workoutplans.js'
// import WorkoutPlans from './component/WorkoutPlans/WorkoutPlans.js';
import CreateWorkoutPlan from './component/WorkoutPlans/CreateWorkoutPlans';
import './css/styles.css'
import Menu from './Menu';


const NewWorkoutPlanPage = () => {
  return (
    <div>
      < Menu />
      <CreateWorkoutPlan />
    </div>
  );
};

export default NewWorkoutPlanPage;