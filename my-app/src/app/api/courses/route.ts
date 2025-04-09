// app/api/courses/route.ts

import { NextResponse } from 'next/server';
import fs from 'fs/promises'; // Use promises version of file system module
import path from 'path';

const COURSES_DIR = path.join(process.cwd(), 'courses_data');
const SLIDES_SUFFIX = '_slides';

export async function GET(request: Request) {
  try {
    // Read the contents of the courses directory
    // { withFileTypes: true } gives us objects telling us if an entry is a directory or file
    const dirents = await fs.readdir(COURSES_DIR, { withFileTypes: true });

    // Filter the results:
    // 1. Keep only directories (dirent.isDirectory())
    // 2. Keep only directories whose names end with '_slides' (dirent.name.endsWith(...))
    const courseFolders = dirents.filter(
      (dirent) => dirent.isDirectory() && dirent.name.endsWith(SLIDES_SUFFIX)
    );

    // Extract the base course name by removing the '_slides' suffix
    const courseNames = courseFolders.map((dirent) =>
      dirent.name.substring(0, dirent.name.length - SLIDES_SUFFIX.length)
    );

    // Return the list of course names in the expected format
    return NextResponse.json({ courses: courseNames });

  } catch (error: any) {
    console.error("API Error fetching courses:", error);

    // Handle specific error: Directory not found
    if (error.code === 'ENOENT') {
      console.warn(`Courses directory not found at: ${COURSES_DIR}`);
      // Return an empty list or a specific error message
      return NextResponse.json({ courses: [] });
      // Or: return NextResponse.json({ message: `Courses directory not found.` }, { status: 404 });
    }

    // Handle other potential errors during file system access
    return NextResponse.json(
      { message: 'Internal Server Error fetching courses list' },
      { status: 500 }
    );
  }
}