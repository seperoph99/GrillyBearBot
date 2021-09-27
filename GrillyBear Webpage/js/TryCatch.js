function TryCatchExample()
{
    try 
    {
        TrYcAtCh();
    }
    catch(error)
    {
        document.getElementById('Err').innerHTML =   error.message;
    }
}