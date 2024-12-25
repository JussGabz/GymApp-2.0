import { useState, useEffect } from "react";
import { fetchExercises } from "../services/exerciseService";

export default function useFetchExercises() {
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            try {
                const result = await fetchExercises()
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