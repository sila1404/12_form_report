import axios from "axios";

export async function getReportData(endPoint: string) {
  try {
    const { data, status } = await axios.get(
      `http://127.0.0.1:8000/reports${endPoint}`
    );

    return {
      data,
      status,
      success: true,
    };
  } catch (error) {
    if (axios.isAxiosError(error)) {
      return {
        data: error.response?.data || null,
        status: error.response?.status || 500,
        success: false,
        message: error.response?.data.error as string,
      };
    }
    // Handle other non-Axios errors if needed
    return {
      data: null,
      status: 500,
      success: false,
      message: "internal server error",
    };
  }
}
