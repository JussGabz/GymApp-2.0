import { useState } from "react"

function WorkoutForm() {

    const [name, setName] = useState("")
    const [loading, setLoading] = useState(false)

    async function handleSubmit(event) {
        event.preventDefault()
        setLoading(true)

        const token = localStorage.getItem('access_token')

        try {
            const response = await fetch("http://127.0.0.1:8000/workoutplans/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(
                    {
                        "name": name,
                        "workout_type": "CARDIO",
                        "exercise_ids": [1],
                     }
                ),
            })

            if (!response.ok) {
                throw new Error("Failed to create workout")
            }

            const data = await response.json()
            alert(`Workout "${data.name}" created successfully!`)
        } catch (error) {
            console.error("Create error:", error)
            alert("Error creating workout")
        } finally {
            setLoading(false)
            setName("")
        }
}

    // function search(event) {
    //     event.preventDefault()
    //     const formData = new FormData(event.target)
    //     const query = formData.get("query")
    //     alert(`You searched for '${query}'`)
    // }
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enter Workout Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
            />
            <button type="submit" disabled={loading}>
                {loading ? "Creatig..." : "Create"}
            </button>
        </form>
    )
}

export default WorkoutForm