import WorkoutPlans from './component/workoutplans.js'
import './css/styles.css'
import Menu from './Menu';


const WorkoutPage = () => {
    return (
      <div>
        < Menu />
        <WorkoutPlans/>
      </div>
    );
  };
  
  export default WorkoutPage;