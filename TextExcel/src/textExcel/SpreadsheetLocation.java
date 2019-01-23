package textExcel;

//Update this file with your own code.

public class SpreadsheetLocation implements Location
{
    String cell;
    
	@Override
    public int getRow()
    {
        // TODO Auto-generated method stub
        return Integer.parseInt(cell.substring(1));
    }

    @Override
    public int getCol()
    {
        // TODO Auto-generated method stub
    	String[] letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    	
        return Character.toUpperCase(cell.charAt(0));
    }
    
    public SpreadsheetLocation(String cellName)
    {
        // TODO: Fill this out with your own code
    	cell = cellName;
    }

}
