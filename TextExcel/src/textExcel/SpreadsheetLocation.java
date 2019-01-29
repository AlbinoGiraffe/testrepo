package textExcel;

//Update this file with your own code.

public class SpreadsheetLocation implements Location
{
    String cell;
    
	@Override
    public int getRow()
    {
        // TODO Auto-generated method stub
		System.out.println(Integer.parseInt(cell.substring(1)));
		return Integer.parseInt(cell.substring(1))-1;
    }

    @Override
    public int getCol()
    {
        // TODO Auto-generated method stub
    	return cell.charAt(0) - 'A';
    }
    
    public SpreadsheetLocation(String cellName)
    {
        // TODO: Fill this out with your own code
    	cell = cellName;
    }

}
