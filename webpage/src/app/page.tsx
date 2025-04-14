"use client";
import Router from "next/navigation";
import React from "react";
import { useState } from "react";
const home = () => {
  const [slideNumber, setSlideNumber] = useState(1);
  const routing = Router.useRouter();
  const route = (page: string) => {
    routing.push(page);
  };

  return (
    <div>
      <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
        {/* Hero Section */}
        <section className="px-4 py-16 text-center">
          <h1 className="mb-4 text-5xl font-bold text-blue-600">
            AI Course Generator
          </h1>
          <p className="mx-auto mb-8 max-w-2xl text-xl text-gray-700">
            Transform your learning journey with AI-generated courses tailored
            to your needs and interests.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button
              className="transform rounded-full bg-blue-600 px-8 py-3 font-medium text-white shadow-lg transition-all hover:scale-105 hover:bg-blue-700"
              onClick={() =>
                alert("Generate course functionality would go here!")
              }
            >
              Generate Your Course
            </button>
            <button
              className="transform rounded-full bg-green-600 px-8 py-3 font-medium text-white shadow-lg transition-all hover:scale-105 hover:bg-green-700"
              onClick={() => alert("Library functionality would go here!")}
            >
              Course Library
            </button>
          </div>
        </section>

        {/* Features Section */}
        <section className="px-4 py-12">
          <h2 className="mb-12 text-center text-3xl font-bold text-gray-800">
            How Our AI Helps You Learn
          </h2>
          <div className="mx-auto grid max-w-6xl grid-cols-1 gap-8 md:grid-cols-3">
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
                className="rounded-xl bg-white p-6 shadow-md transition-shadow hover:shadow-lg"
              >
                <div className="mb-4 text-4xl">{card.icon}</div>
                <h3 className="mb-2 text-xl font-semibold text-gray-800">
                  {card.title}
                </h3>
                <p className="text-gray-600">{card.description}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Call to Action */}
        <section className="bg-blue-50 px-4 py-16 text-center">
          <h2 className="mb-4 text-3xl font-bold text-gray-800">
            Ready to Transform Your Learning?
          </h2>
          <p className="mx-auto mb-8 max-w-2xl text-xl text-gray-700">
            Join thousands of learners who have accelerated their education with
            our AI-powered courses.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button
              className="transform rounded-full bg-blue-600 px-8 py-3 font-medium text-white shadow-lg transition-all hover:scale-105 hover:bg-blue-700"
              onClick={() => route("/generate")}
            >
              Get Started Now
            </button>
            <button
              className="transform rounded-full bg-green-600 px-8 py-3 font-medium text-white shadow-lg transition-all hover:scale-105 hover:bg-green-700"
              onClick={() => route("/library")}
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
