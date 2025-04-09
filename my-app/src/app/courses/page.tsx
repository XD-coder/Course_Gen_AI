"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";

const CoursesPage = () => {
  // State hooks are correct
  const [courses, setCourses] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchCourses() {
      setLoading(true);
      setError(null);
      try {
        const response = await fetch("/api/courses");

        if (!response.ok) {
          throw new Error(
            `Failed to fetch courses: ${response.statusText} (Status: ${response.status})`
          );
        }

        // Parse the JSON response from the API
        const data = await response.json();

        // Check if the expected 'courses' array exists in the response
        if (!data || !Array.isArray(data.courses)) {
          console.error("API response format incorrect:", data);
          throw new Error("Received invalid data format from server.");
        }

        // Update the component state with the fetched course names
        setCourses(data.courses);
      } catch (err: any) {
        // Catch any errors during fetch or processing
        setError(`Error loading courses: ${err.message}`);
        console.error("Fetch courses error:", err);
        setCourses([]); // Clear courses on error
      } finally {
        // Always set loading to false after the fetch attempt finishes
        setLoading(false);
      }
    }

    // Call the async function defined inside useEffect
    fetchCourses();
  }, []); // Empty dependency array means this effect runs once on mount

  // Conditional rendering based on state is correct
  if (loading) return <div className="p-4 text-center">Loading courses...</div>;
  if (error)
    return (
      <div className="p-4 text-red-600 bg-red-100 border border-red-400 rounded text-center">
        {error}
      </div>
    );

  // Rendering the list of courses is correct
  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Available Courses</h1>

      {courses.length === 0 ? (
        <p className="text-center text-gray-500">No courses found.</p>
      ) : (
        <ul className="space-y-3">
          {/* Use course name as key if unique, otherwise index is fallback */}
          {courses.map((course) => (
            <li
              key={course} // Using course name as key is often more stable than index
              className="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow"
            >
              <Link
                href={`/courses/${course}`} // Assumes dynamic route like /courses/[courseName]
                className="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors"
              >
                {/* Simple title case for display */}
                <span className="text-xl font-medium capitalize">
                  {course.replace(/_/g, " ")}
                </span>
                <span className="text-blue-600 font-semibold text-sm">
                  View Course →
                </span>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default CoursesPage;
