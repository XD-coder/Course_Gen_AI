"use client";

import React from "react";
import { useState } from "react";
const home = () => {
  const [slideNumber, setSlideNumber] = useState(1);
  return (
    <div>
      <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
        {/* Hero Section */}
        <section className="text-center py-16 px-4">
          <h1 className="text-5xl font-bold mb-4 text-blue-600">
            AI Course Generator
          </h1>
          <p className="text-xl text-gray-700 max-w-2xl mx-auto mb-8">
            Transform your learning journey with AI-generated courses tailored
            to your needs and interests.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-8 rounded-full shadow-lg transition-all transform hover:scale-105"
              onClick={() =>
                alert("Generate course functionality would go here!")
              }
            >
              Generate Your Course
            </button>
            <button
              className="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-8 rounded-full shadow-lg transition-all transform hover:scale-105"
              onClick={() => alert("Library functionality would go here!")}
            >
              Course Library
            </button>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-12 px-4">
          <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">
            How Our AI Helps You Learn
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {[
              {
                title: "Personalized Learning",
                description:
                  "Custom courses built around your specific goals, learning style, and knowledge level.",
                icon: "🎯",
              },
              {
                title: "Save Time",
                description:
                  "Get a structured learning path instantly instead of spending hours searching for resources.",
                icon: "⏱️",
              },
              {
                title: "Quality Content",
                description:
                  "Access expertly curated materials from trusted sources across the web.",
                icon: "✅",
              },
              {
                title: "Interactive Exercises",
                description:
                  "Practice what you learn with tailored exercises that reinforce your knowledge.",
                icon: "📝",
              },
              {
                title: "Track Progress",
                description:
                  "Monitor your advancement and receive suggestions for improvement.",
                icon: "📈",
              },
              {
                title: "Learn Anywhere",
                description:
                  "Access your personalized courses on any device, anytime, anywhere.",
                icon: "🌐",
              },
            ].map((card, index) => (
              <div
                key={index}
                className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow"
              >
                <div className="text-4xl mb-4">{card.icon}</div>
                <h3 className="text-xl font-semibold mb-2 text-gray-800">
                  {card.title}
                </h3>
                <p className="text-gray-600">{card.description}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Call to Action */}
        <section className="text-center py-16 px-4 bg-blue-50">
          <h2 className="text-3xl font-bold mb-4 text-gray-800">
            Ready to Transform Your Learning?
          </h2>
          <p className="text-xl text-gray-700 max-w-2xl mx-auto mb-8">
            Join thousands of learners who have accelerated their education with
            our AI-powered courses.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-8 rounded-full shadow-lg transition-all transform hover:scale-105"
              onClick={() => setSlideNumber(2)}
            >
              Get Started Now
            </button>
            <button
              className="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-8 rounded-full shadow-lg transition-all transform hover:scale-105"
              onClick={() => alert("Browse existing courses in our library")}
            >
              Browse Library
            </button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default home;
