
// import WorkoutPlans from './component/workoutplans.js'
import WorkoutPlans from './component/WorkoutPlans/WorkoutPlans.js';
import './css/styles.css'
import Menu from './Menu';


const WorkoutPage = () => {
  return (
    <div>
      < Menu />
      <WorkoutPlans />
    </div>
  );
};

export default WorkoutPage;