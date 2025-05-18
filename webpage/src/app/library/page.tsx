"use client";
import React, { useEffect, useState } from "react";

const Library = () => {
  const [slideHtml, setSlideHtml] = useState<string | null>(null);
  const slideId = 1; // Or dynamically set this from URL

  useEffect(() => {
    const fetchSlide = async () => {
      const response = await fetch(`http://127.0.0.1:8000/slides/${slideId}`);
      const data = await response.text();
      setSlideHtml(data);
    };

    fetchSlide();
  }, [slideId]);

  return (
    <div className="flex h-screen w-full flex-col items-center justify-center">
      <h1 className="mb-4 text-4xl font-bold">Library</h1>
      {slideHtml ? (
        <div dangerouslySetInnerHTML={{ __html: slideHtml }} />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Library;
