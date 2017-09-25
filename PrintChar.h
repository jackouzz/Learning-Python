int PrintChar ( char * string )
{
    //int i;
    char temp;
    temp = *string;
    if (temp == '\0')
    {
        return (-1);
    }
    while (temp != '\0')
    {
        printf ("%c /n",temp);
        string++;
        temp = *string;
    }
    return(0);
//仅仅是测试是不够的
}
