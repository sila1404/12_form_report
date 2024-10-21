import { Button, buttonVariants } from "./ui/button";
import { Popover, PopoverTrigger, PopoverContent } from "./ui/popover";
import { exportToExcel, exportToCSV } from "@/lib/exportFile";

type Props = {
  data: any;
  sheetName: string;
  fileName: string;
};

const DownloadButton = (props: Props) => {
  return (
    <div className="fixed bottom-8 right-8">
      <Popover>
        <PopoverTrigger asChild>
          <Button className="ml-32 font-bold bg-blue-600 hover:bg-blue-700">
            Download
          </Button>
        </PopoverTrigger>
        <PopoverContent>
          <div className="flex flex-col gap-3">
            <Button
              className="bg-blue-600 hover:bg-blue-700"
              onClick={() =>
                exportToExcel(props.data, props.sheetName, props.fileName)
              }
            >
              Excel
            </Button>
            <Button
              className="bg-blue-600 hover:bg-blue-700"
              onClick={() => exportToCSV(props.data, props.fileName)}
            >
              CSV
            </Button>
            <Button className={buttonVariants({ variant: "destructive" })}>
              PDF (Coming Soon)
            </Button>
          </div>
        </PopoverContent>
      </Popover>
    </div>
  );
};

export default DownloadButton;