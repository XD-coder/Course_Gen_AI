import React from "react";

const page = async ({ params }: { params: Promise<{ course_id: string }> }) => {
  const { course_id } = await params;
  console.log("course_id", course_id);
  if (!course_id) {
    return <div>Course not found</div>;
  }

  return <div></div>;
};

export default page;
