import { useEffect, useState } from "react";
import { EXERCISES_ENDPOINT } from "../../config/apiConfig";
import { fetchExercises } from "../../services/exerciseService";

function ExerciseDropdown() {
    const [exercises, setExercises] = useState([])
    const [selected, setSelected] = useState([])
    const [url, setCurrentUrl] = useState(EXERCISES_ENDPOINT)

    useEffect(() => {
        fetchExercise(url)
    }, [url])

    const fetchExercise = async (url) => {
        try {
            const response = await fetchExercises(url)
            setExercises(response.results)
        } catch (error) {
            console.error('Error Fetching exercise Data:', error)
        } finally {
        }
    }

    function handleChange(id) {
        setSelected(prev =>
            prev.includes(id) ? prev.filter(item => item !== id) : [...prev, id]
        )
    }

    return (
        <div>
            {exercises.map((exercise) => (
                <label key={exercise.id}>
                    <input
                        type="checkbox"
                        value={exercise.id}
                        checked={selected.includes(exercise.id)}
                        onChange={() => handleChange(exercise.id)}
                    />
                    {exercise.name}
                </label>
            ))}
        </div>
    )
}

export default ExerciseDropdown