import React from "react";

const library = () => {
  return (
    <div className="flex h-screen w-full items-center justify-center">
      <h1 className="text-4xl font-bold">Library</h1>
      <iframe
        src="localhost:3000/AI_with_python/slides/slide_2.html"
        className="h-screen w-full"
      ></iframe>
    </div>
  );
};

export default library;
