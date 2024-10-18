import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/f3")({
  component: ReportF3,
});

function ReportF3() {
  return (<div className="w-screen grid place-items-center">Coming soon</div>);
}
