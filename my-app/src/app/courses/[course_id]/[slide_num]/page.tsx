import React from "react";

const slide = async ({
  params,
}: {
  params: Promise<{ course_id: string; slide_num: number }>;
}) => {
  const { course_id, slide_num } = await params;
  console.log("course_id", course_id);
  console.log("slide_num", slide_num);

  return <div>slide page</div>;
};

export default slide;
