import { useState, useEffect } from "react";
import { fetchWorkoutPlans } from "../services/workoutplanService";

export default function useFetchWorkoutPlans() {
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() =>{
        const fetchData = async () => {
            try {
                const result = await fetchWorkoutPlans()
                setData(result)
            } catch (err) {
                setError(err.message)
            } finally {
                setLoading(false)
            }
        }
        fetchData();
    }, [])

    return { data, loading, error}
}