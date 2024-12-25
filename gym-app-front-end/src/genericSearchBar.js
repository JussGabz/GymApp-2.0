// Generic Search Bar 
//  Placeholder -> Custom Text for input
// Value -> Current Search input value, controlled by the parent component
// onChange -> Callback function triggered when the search input value changes
// onSearch -> Callback function to handle the search action 


import React from "react";

function SearchBar({ placeholder = 'Search...', value, onChange, onSearch}) {
    const handleInputChange = (event) => {
        onChange(event.target.value)
    }

    const handleSearch = () => {
        if (onSearch) {
            onSearch(value)
        }
    }

    return (
        <div className="search-bar">
            <input
                type="text"
                className="search-input"
                placeholder={placeholder}
                value={value}
                onChange={handleInputChange}
            />
            <button className="search-button" onClick={handleSearch}>
                Search
            </button>
        </div>
    )
}

export default SearchBar