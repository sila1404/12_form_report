type Props = {
  reportMessage: string
};

const ReportHeader = (props: Props) => {
  return (
    <>
      <div className="flex flex-col items-center text-sm font-bold">
        <h4>ສາທາລະນະລັດ ປະຊາທິປະໄຕ ປະຊາຊົນລາວ</h4>
        <h4>ສັນຕິພາບ ເອກະລາດ ປະຊາທິປະໄຕ ເອກະພາບ ວັດທະນະຖາວອນ</h4>
      </div>
      <div className="flex flex-col items-center my-7 text-xl font-bold">
        <h1>ໃບລາຍງານ</h1>
        <h1>{props.reportMessage}</h1>
      </div>
    </>
  );
};

export default ReportHeader;
