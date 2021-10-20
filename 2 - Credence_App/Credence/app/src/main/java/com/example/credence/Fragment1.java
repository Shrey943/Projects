package com.example.credence;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.app.Dialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.DialogFragment;
import androidx.fragment.app.Fragment;

import com.example.credence.R;

public class Fragment1 extends Fragment {


//    private static final String SHARED_PREF_NAME = "mypref";

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment1_layout,container,false);


        final EditText text1 = view.findViewById(R.id.editTextTextPersonName);
        final EditText text2 = view.findViewById(R.id.editTextTextPersonName2);
        final EditText text3 = view.findViewById(R.id.editText3);
        final EditText text4 = view.findViewById(R.id.editText4);
        final EditText text5 = view.findViewById(R.id.editText5);
        final TextView textView3 =view.findViewById(R.id.textView3);
        final TextView textView4 =view.findViewById(R.id.textView4);
        final TextView textView5 =view.findViewById(R.id.textView5);
        final TextView textView6 =view.findViewById(R.id.textView6);
        final ImageButton help1 = view.findViewById(R.id.help1);
        final ImageView help2 = view.findViewById(R.id.help2);
        final LinearLayout create = view.findViewById(R.id.create);
        final Button button  = view.findViewById(R.id.submit);
        final Button update  = view.findViewById(R.id.update);
        final Button addComment  = view.findViewById(R.id.addComment);
        final ScrollView scrollView = view.findViewById(R.id.scroll);
//        scrollView.setClickable(false);
//        create.removeView(textView3);
//        create.removeView(textView4);
//        create.removeView(textView5);
//        create.removeView(textView6);
//        create.removeView(text3);
//        create.removeView(text4);
//        create.removeView(text5);
        final int[] a = {0};

//        final Dialog dialog1 = new Dialog(getContext());

        help1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showDialog();

            }
        });



        button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                if (a[0] ==0) {

                    final String Text1 = text1.getText().toString();
                    final String Text2 = text2.getText().toString();
                    if (Text1.length() == 0 || Text2.length() == 0) {
                        Toast toast = Toast.makeText(getActivity(), "Values can't be empty", Toast.LENGTH_SHORT);
                        toast.show();
                    } else if (Float.parseFloat(Text2) >= 100 || Float.parseFloat(Text2) <= 0) {

                        Toast toast = Toast.makeText(getActivity(), "Values in percentage must lie between 0 to 100 only.", Toast.LENGTH_SHORT);
                        toast.show();
                    } else {

                        float per1 = Float.parseFloat(Text2);
                        float per = (float) (Math.round(per1 * 10) / 10.0);

                            SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);


                            if (shrd.getBoolean("my_first_time", true)) {
                                SharedPreferences.Editor editor = shrd.edit();
                                editor.putInt("id", 1);
                                editor.apply();

                                shrd.edit().putBoolean("my_first_time", false).commit();

                            }
                            int n = shrd.getInt("id", 1);

                            SharedPreferences.Editor editor = shrd.edit();

                            editor.putString("belief" + n, Text1);
                            editor.putFloat("per" + n, per);
                            editor.putInt("id", n + 1);
                            editor.apply();

                            Intent intent = getActivity().getIntent();
                            getActivity().finish();
                            startActivity(intent);
//                        getActivity().finish();


                            Toast toast = Toast.makeText(getActivity(), "Created credence: " + per + "%", Toast.LENGTH_LONG);
                            toast.show();

                        }


                }
                else if(a[0]==4){

                    final String Text1 = text1.getText().toString();
                    final String Text2 = text2.getText().toString();
                    final String Text3 = text5.getText().toString();

                    if( Text1.length() == 0 ||Text2.length() == 0 || Text3.length()==0){
                        Toast toast = Toast.makeText(getActivity(),"Values can't be empty",Toast.LENGTH_SHORT);
                        toast.show();
                    }
                    else if (Float.parseFloat(Text2) >= 100 || Float.parseFloat(Text2) <= 0 ){

                        Toast toast = Toast.makeText(getActivity(),"Values in percentage must lie between 0 to 100 only.",Toast.LENGTH_SHORT);
                        toast.show();
                    }
                    else {

                        float per1 = Float.parseFloat(Text2);
                        float per = (float) (Math.round(per1 * 10) / 10.0);

                            SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);


                            if (shrd.getBoolean("my_first_time", true)) {
                                SharedPreferences.Editor editor = shrd.edit();
                                editor.putInt("id", 1);
                                editor.apply();

                                shrd.edit().putBoolean("my_first_time", false).commit();

                            }
                            int n = shrd.getInt("id", 1);

                            SharedPreferences.Editor editor = shrd.edit();

                            editor.putString("belief" + n, Text1);
                            editor.putFloat("per" + n, per);
                            editor.putString("comment" + n, Text3);
                            editor.putInt("id", n + 1);
                            editor.apply();

                            Intent intent = getActivity().getIntent();
                            getActivity().finish();
                            startActivity(intent);
//                        getActivity().finish();


                            Toast toast = Toast.makeText(getActivity(), "Created credence: " + per + "%", Toast.LENGTH_LONG);
                            toast.show();


                    }

                }
                else if(a[0]==5){


                    final String Text1 = text1.getText().toString();
                    final String Text2 = text2.getText().toString();
                    final String Text3 = text3.getText().toString();
                    final String Text4 = text4.getText().toString();



                    if( Text1.length() == 0 ||Text2.length() == 0 ||Text3.length() == 0||Text4.length() == 0){
                        Toast toast = Toast.makeText(getActivity(),"Values can't be empty",Toast.LENGTH_SHORT);
                        toast.show();
                    }

                    else if (Float.parseFloat(Text2) >= 100 || Float.parseFloat(Text2) <= 0 ||Float.parseFloat(Text3) <= 0 ||Float.parseFloat(Text4) <= 0 || Float.parseFloat(Text3)>=100 || Float.parseFloat(Text4)>=100){

                        Toast toast = Toast.makeText(getActivity(),"Values in percentage must lie between 0 to 100 only.",Toast.LENGTH_SHORT);
                        toast.show();
                    }
                    else {


                        float N1 = Float.parseFloat(Text2) / 100;
                        float N2 = Float.parseFloat(Text3) / 100;
                        float N3 = Float.parseFloat(Text4) / 100;


                        float a = N1 / (1 - N1);
                        float b = N2 / N3;
                        float c = 1 + a * b;
                        float d = a * b / c;

                        float perPre = d * 100;
                        float per = (float) (Math.round(perPre * 10) / 10.0);

                            SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);


                            if (shrd.getBoolean("my_first_time", true)) {
                                SharedPreferences.Editor editor = shrd.edit();
                                editor.putInt("id", 1);
                                editor.apply();

                                shrd.edit().putBoolean("my_first_time", false).commit();

                            }
                            int n = shrd.getInt("id", 1);

                            SharedPreferences.Editor editor = shrd.edit();

                            editor.putString("belief" + n, Text1);
                            editor.putFloat("per" + n, per);

                            editor.putInt("id", n + 1);
                            editor.apply();

                            Intent intent = getActivity().getIntent();
                            getActivity().finish();
                            startActivity(intent);


                            Toast toast = Toast.makeText(getActivity(), "Created credence: " + per + "%", Toast.LENGTH_LONG);
                            toast.show();

                    }




                }

                else {

                    final String Text1 = text1.getText().toString();
                    final String Text2 = text2.getText().toString();
                    final String Text3 = text3.getText().toString();
                    final String Text4 = text4.getText().toString();
                    final String Text5 = text5.getText().toString();


                    if( Text1.length() == 0 ||Text2.length() == 0 ||Text3.length() == 0||Text4.length() == 0 ||Text5.length()==0){
                    Toast toast = Toast.makeText(getActivity(),"Values can't be empty",Toast.LENGTH_SHORT);
                    toast.show();
                    }

                    else if (Float.parseFloat(Text2) >= 100 || Float.parseFloat(Text2) <= 0 ||Float.parseFloat(Text3) <= 0 ||Float.parseFloat(Text4) <= 0 || Float.parseFloat(Text3)>=100 || Float.parseFloat(Text4)>=100){

                    Toast toast = Toast.makeText(getActivity(),"Values in percentage must lie between 0 to 100 only.",Toast.LENGTH_SHORT);
                    toast.show();
                    }
                else {


                    float N1 = Float.parseFloat(Text2) / 100;
                    float N2 = Float.parseFloat(Text3) / 100;
                    float N3 = Float.parseFloat(Text4) / 100;


                    float a = N1 / (1 - N1);
                    float b = N2 / N3;
                    float c = 1 + a * b;
                    float d = a * b / c;

                    float perPre = d * 100;
                    float per = (float) (Math.round(perPre * 10) / 10.0);

                    SharedPreferences shrd = getActivity().getSharedPreferences("demo", Context.MODE_PRIVATE);


                        if (shrd.getBoolean("my_first_time", true)) {
                            SharedPreferences.Editor editor = shrd.edit();
                            editor.putInt("id", 1);
                            editor.apply();

                            shrd.edit().putBoolean("my_first_time", false).commit();

                        }
                        int n = shrd.getInt("id", 1);

                        SharedPreferences.Editor editor = shrd.edit();

                        editor.putString("belief" + n, Text1);
                        editor.putFloat("per" + n, per);
                        editor.putString("comment" + n, Text5);
                        editor.putInt("id", n + 1);
                        editor.apply();

                        Intent intent = getActivity().getIntent();
                        getActivity().finish();
                        startActivity(intent);


                        Toast toast = Toast.makeText(getActivity(), "Created credence: " + per + "%", Toast.LENGTH_LONG);
                        toast.show();

                }


                }
            }
        });
        update.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                create.removeView(button);
                create.removeView(addComment);
//                create.addView(text3);
//                create.addView(text4);
//                create.addView(textView3);
//                create.addView(textView4);
//                create.addView(textView5);
//                create.addView(textView3);

                text3.setAlpha(1f);
                text4.setAlpha(1f);
//                text5.setAlpha(1f);
                textView3.setAlpha(1f);
                textView4.setAlpha(1f);
                textView5.setAlpha(1f);
//                textView6.setAlpha(1f);
                help2.setAlpha((1f));
                help2.setClickable(true);
                text3.setClickable(true);
                text4.setClickable(true);
//                scrollView.setClickable(true);
//                text5.setClickable(true);

//                LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, 66);
//                params.setMargins(50,30,50,5);
//                Button submit = new Button(getContext());
//                submit.setLayoutParams(params);
//
//                submit.setId(Integer.parseInt("submit"));
//                submit.setText("SUBMIT");
//                submit.setTextSize(20);
                if(a[0]==0) {
                    create.removeView(textView6);
                    create.removeView(text5);
                    create.addView(button, 10);
                    create.addView(addComment, 11);

                }
                else{
                    create.removeView(textView6);
                    create.removeView(text5);
//                    int Id1 = getResources().getIdentifier("textView6","id",getActivity().getPackageName());
//                    int Id2 = getResources().getIdentifier("editText5","id",getActivity().getPackageName());
//                    TextView textView = view.findViewById(Id1);
//                    EditText editText = view.findViewById(Id2);
                    create.addView(textView6, 10);
                    create.addView(text5, 11);
                    create.addView(button, 12);


                }
                create.removeView(update);
                a[0] =a[0]+5;

            }
        });

//        final Dialog dialog2 = new Dialog(getActivity());

        help2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showDialog2();
//
            }
        });
        addComment.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                text5.setAlpha(1f);
                textView6.setAlpha(1f);
                text5.setClickable(true);


                //                LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
//                LinearLayout.LayoutParams params2 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, 47);
//                params.setMargins(10,25,0,5);
//                params2.setMargins(10,5,10,0);
//
//                TextView add_comment2 = new TextView(getContext());
//                add_comment2.setId(Integer.parseInt("textView6"));
//                add_comment2.setLayoutParams(params);
//                add_comment2.setText("Add a comment:");
//                add_comment2.setTextSize(20);
//                add_comment2.setPadding(10,0,0,0);
//                add_comment2.setTextColor(getResources().getColor(R.color.white));
//
//                EditText editComment = new EditText(getContext());
//                editComment.setId(Integer.parseInt("editText5"));
//                editComment.setLayoutParams(params2);
//                editComment.setPadding(15,0,0,0);
//                editComment.setHint("Enter comment");
//                editComment.setTextSize(20);
//                editComment.setEms(10);
//                editComment.setBackgroundColor(getResources().getColor(R.color.white));

                if(a[0]==0){
                    create.removeView(text5);
                    create.removeView(textView6);
                    create.addView(textView6,4);
                    create.addView(text5,5);
                }
                else {
                    create.removeView(button);
                    create.addView(textView6,10);
                    create.addView(text5,11);
                    create.addView(button,12);
                }

                create.removeView(addComment);
                a[0]=a[0]+4;

            }
        });

        return view;

    }
    void showDialog(){

        LayoutInflater inflater = LayoutInflater.from(getContext());
        View view = inflater.inflate(R.layout.help_text,null);

        AlertDialog alertDialog = new AlertDialog.Builder(getContext()).setView(view).create();

        alertDialog.show();
        alertDialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));


    }
    void showDialog2(){

        LayoutInflater inflater = LayoutInflater.from(getContext());
        View view = inflater.inflate(R.layout.help_text2,null);

        AlertDialog alertDialog = new AlertDialog.Builder(getContext()).setView(view).create();

        alertDialog.show();
        alertDialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));
//        alertDialog.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_DIM_BEHIND);

    }







}
