import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/f9")({
  component: ReportF9,
});

function ReportF9() {
  return <div className="w-screen grid place-items-center">Coming soon</div>;
}
