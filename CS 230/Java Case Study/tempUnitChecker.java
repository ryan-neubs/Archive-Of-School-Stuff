package tempConverter;

public class tempUnitChecker {
	
	boolean checkTempUnit(char TempUnit) {	//check that the temperature unit is correct
		switch(TempUnit) {
		default:
			return false;
		case 'c':
			return true;
		case 'f':
			return true;
		case 'k':
			return true;
		}
	}

}
