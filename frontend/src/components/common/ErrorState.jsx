export default function ErrorState({

    message
}) {

    return (

        <div className="bg-red-100 border border-red-300 rounded-2xl p-6">

            <h2 className="text-red-700 text-xl font-bold">

                Something Went Wrong
            </h2>

            <p className="text-red-600 mt-2">

                {message}
            </p>
        </div>
    );
}