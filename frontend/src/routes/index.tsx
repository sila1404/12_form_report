import { createFileRoute, redirect } from "@tanstack/react-router";

const isImported = false;

export const Route = createFileRoute("/")({
  loader: () => {
    if (isImported) {
      throw redirect({
        to: "/f2",
      });
    }
  },
  component: Root
});

function Root() {
  return (
    <>
      <h1 className="w-screen grid place-items-center">Import the file to see the report.</h1>
    </>
  )
}
