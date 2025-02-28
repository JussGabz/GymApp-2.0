import React, { useState } from "react";
import SearchBar from "../../genericSearchBar";

function WorkoutPlanSearchBar({ onSearch }) {
    const [searchQuery, setSearchQuery] = useState('')

    const handleSearchChange = (newValue) => {
        setSearchQuery(newValue)
    }

    const handleSearch = async (query) => {
        console.log(`Searching for: ${query}`)

        const data = onSearch(searchQuery)

        console.log(data)
    }

    return (
        <div className="workoutplan-search">
            <SearchBar
                placeholder="Search Workout Plan..."
                value={searchQuery}
                onChange={handleSearchChange}
                onSearch={handleSearch}
            />
        </div>
    )
}

export default WorkoutPlanSearchBar