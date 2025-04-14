import { NextRequest, NextResponse } from "next/server";
import fs from "fs";
import path from "path";

export const dynamic = "force-dynamic";

export async function GET(req: NextRequest) {
  try {
    // Define the path to the course_data directory
    const courseDataPath = path.join(process.cwd(), "course_data");

    // Check if directory exists
    if (!fs.existsSync(courseDataPath)) {
      return NextResponse.json(
        { error: "Course data directory not found" },
        { status: 404 },
      );
    }

    // Read the directory
    const items = fs.readdirSync(courseDataPath);

    // Filter out only folders
    const folders = items.filter((item) => {
      const itemPath = path.join(courseDataPath, item);
      return fs.statSync(itemPath).isDirectory();
    });

    // Return the folder names
    return NextResponse.json({ folders });
  } catch (error) {
    console.error("Error fetching course folders:", error);
    return NextResponse.json(
      { error: "Failed to fetch course folders" },
      { status: 500 },
    );
  }
}
