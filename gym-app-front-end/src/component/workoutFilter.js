
import { Dropdown } from 'react-bootstrap'

const WorkoutDropDown = () => (
<Dropdown>
    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
        Workout Category
    </Dropdown.Toggle>
    <Dropdown.Menu>
        <Dropdown.Item href="http://127.0.0.1:8000/workoutplans/">Chest</Dropdown.Item>
        <Dropdown.Item href="#/action-2">Back</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Legs</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Abs</Dropdown.Item>
    </Dropdown.Menu>
</Dropdown>
)

export default WorkoutDropDown